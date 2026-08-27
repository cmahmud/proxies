# SyndProxy validated proxy pool

## Current pool

- Alive now: 672
- Gold now: 419
- HTTP: 127 alive / 72 gold
- HTTPS: 185 alive / 23 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40492
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
