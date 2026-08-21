# SyndProxy private pool

## Current pool

- Alive now: 1134
- Gold now: 427
- HTTP: 377 alive / 109 gold
- HTTPS: 225 alive / 31 gold
- SOCKS4: 260 alive / 147 gold
- SOCKS5: 272 alive / 140 gold

## Historical pool

- Discovered: 160278
- Ever alive: 30780
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
