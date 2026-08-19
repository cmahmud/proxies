# SyndProxy private pool

## Current pool

- Alive now: 1345
- Gold now: 430
- HTTP: 481 alive / 93 gold
- HTTPS: 342 alive / 24 gold
- SOCKS4: 230 alive / 150 gold
- SOCKS5: 292 alive / 163 gold

## Historical pool

- Discovered: 136206
- Ever alive: 22389
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
