# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 402
- HTTP: 337 alive / 88 gold
- HTTPS: 232 alive / 27 gold
- SOCKS4: 199 alive / 132 gold
- SOCKS5: 231 alive / 155 gold

## Historical pool

- Discovered: 144731
- Ever alive: 24934
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
