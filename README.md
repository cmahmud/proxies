# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 402
- HTTP: 96 alive / 58 gold
- HTTPS: 94 alive / 19 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43017
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
