# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 405
- HTTP: 107 alive / 65 gold
- HTTPS: 68 alive / 18 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 192 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38673
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
