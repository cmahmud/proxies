# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 380
- HTTP: 142 alive / 61 gold
- HTTPS: 44 alive / 15 gold
- SOCKS4: 169 alive / 152 gold
- SOCKS5: 173 alive / 152 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33210
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
