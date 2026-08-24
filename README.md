# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 384
- HTTP: 121 alive / 66 gold
- HTTPS: 50 alive / 13 gold
- SOCKS4: 171 alive / 152 gold
- SOCKS5: 175 alive / 153 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33221
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
