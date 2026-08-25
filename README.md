# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 395
- HTTP: 92 alive / 64 gold
- HTTPS: 69 alive / 20 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37507
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
