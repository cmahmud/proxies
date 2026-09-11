# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 402
- HTTP: 91 alive / 66 gold
- HTTPS: 35 alive / 19 gold
- SOCKS4: 159 alive / 146 gold
- SOCKS5: 183 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48806
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
