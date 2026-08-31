# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 453
- HTTP: 127 alive / 82 gold
- HTTPS: 123 alive / 36 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45627
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
