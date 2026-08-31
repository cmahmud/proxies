# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 450
- HTTP: 123 alive / 84 gold
- HTTPS: 101 alive / 33 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 206 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45579
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
