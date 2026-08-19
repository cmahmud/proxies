# SyndProxy private pool

## Current pool

- Alive now: 1135
- Gold now: 538
- HTTP: 423 alive / 164 gold
- HTTPS: 272 alive / 88 gold
- SOCKS4: 217 alive / 140 gold
- SOCKS5: 223 alive / 146 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18640
- Ever gold: 722

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
