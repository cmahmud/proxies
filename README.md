# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 362
- HTTP: 109 alive / 37 gold
- HTTPS: 51 alive / 10 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 186 alive / 155 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32926
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
