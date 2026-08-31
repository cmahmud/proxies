# SyndProxy validated proxy pool

## Current pool

- Alive now: 663
- Gold now: 478
- HTTP: 171 alive / 104 gold
- HTTPS: 125 alive / 39 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 199 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45208
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
