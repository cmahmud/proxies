# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 436
- HTTP: 127 alive / 84 gold
- HTTPS: 141 alive / 19 gold
- SOCKS4: 184 alive / 164 gold
- SOCKS5: 192 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42238
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
