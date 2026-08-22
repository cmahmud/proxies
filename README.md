# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 428
- HTTP: 299 alive / 90 gold
- HTTPS: 230 alive / 32 gold
- SOCKS4: 209 alive / 142 gold
- SOCKS5: 240 alive / 164 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31241
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
