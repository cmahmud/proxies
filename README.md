# SyndProxy private pool

## Current pool

- Alive now: 1177
- Gold now: 538
- HTTP: 458 alive / 154 gold
- HTTPS: 299 alive / 105 gold
- SOCKS4: 211 alive / 133 gold
- SOCKS5: 209 alive / 146 gold

## Historical pool

- Discovered: 127351
- Ever alive: 19832
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
