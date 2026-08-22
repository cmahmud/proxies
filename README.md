# SyndProxy private pool

## Current pool

- Alive now: 750
- Gold now: 406
- HTTP: 194 alive / 88 gold
- HTTPS: 150 alive / 27 gold
- SOCKS4: 189 alive / 137 gold
- SOCKS5: 217 alive / 154 gold

## Historical pool

- Discovered: 162443
- Ever alive: 31440
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
