# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 402
- HTTP: 106 alive / 69 gold
- HTTPS: 51 alive / 12 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 196 alive / 163 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33333
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
