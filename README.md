# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 387
- HTTP: 106 alive / 68 gold
- HTTPS: 43 alive / 14 gold
- SOCKS4: 164 alive / 152 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33243
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
