# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 386
- HTTP: 134 alive / 48 gold
- HTTPS: 52 alive / 13 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33582
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
