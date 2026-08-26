# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 414
- HTTP: 108 alive / 71 gold
- HTTPS: 77 alive / 19 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37940
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
