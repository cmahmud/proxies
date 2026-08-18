# SyndProxy private pool

## Current pool

- Alive now: 1131
- Gold now: 302
- HTTP: 440 alive / 31 gold
- HTTPS: 249 alive / 4 gold
- SOCKS4: 231 alive / 140 gold
- SOCKS5: 211 alive / 127 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13416
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
