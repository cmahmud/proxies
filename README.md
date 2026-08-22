# SyndProxy private pool

## Current pool

- Alive now: 824
- Gold now: 386
- HTTP: 266 alive / 96 gold
- HTTPS: 154 alive / 27 gold
- SOCKS4: 202 alive / 135 gold
- SOCKS5: 202 alive / 128 gold

## Historical pool

- Discovered: 162755
- Ever alive: 31582
- Ever gold: 1162

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
