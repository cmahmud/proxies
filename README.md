# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 254
- HTTP: 223 alive / 32 gold
- HTTPS: 151 alive / 8 gold
- SOCKS4: 224 alive / 135 gold
- SOCKS5: 185 alive / 79 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9679
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
