# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 406
- HTTP: 106 alive / 64 gold
- HTTPS: 67 alive / 21 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 184 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38737
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
