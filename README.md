# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 449
- HTTP: 122 alive / 83 gold
- HTTPS: 91 alive / 33 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 204 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45578
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
