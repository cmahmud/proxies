# SyndProxy validated proxy pool

## Current pool

- Alive now: 453
- Gold now: 362
- HTTP: 75 alive / 41 gold
- HTTPS: 32 alive / 8 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 182 alive / 158 gold

## Historical pool

- Discovered: 173056
- Ever alive: 33004
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
