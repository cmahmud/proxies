# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 417
- HTTP: 97 alive / 68 gold
- HTTPS: 88 alive / 19 gold
- SOCKS4: 176 alive / 164 gold
- SOCKS5: 176 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37828
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
