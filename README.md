# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 426
- HTTP: 112 alive / 82 gold
- HTTPS: 144 alive / 18 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42294
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
