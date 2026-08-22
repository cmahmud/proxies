# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 410
- HTTP: 347 alive / 93 gold
- HTTPS: 205 alive / 23 gold
- SOCKS4: 228 alive / 135 gold
- SOCKS5: 257 alive / 159 gold

## Historical pool

- Discovered: 166609
- Ever alive: 32426
- Ever gold: 1181

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
