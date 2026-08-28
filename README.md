# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 439
- HTTP: 126 alive / 84 gold
- HTTPS: 144 alive / 21 gold
- SOCKS4: 186 alive / 164 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42238
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
