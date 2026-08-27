# SyndProxy validated proxy pool

## Current pool

- Alive now: 672
- Gold now: 418
- HTTP: 128 alive / 72 gold
- HTTPS: 186 alive / 23 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40489
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
