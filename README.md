# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 425
- HTTP: 104 alive / 74 gold
- HTTPS: 74 alive / 21 gold
- SOCKS4: 187 alive / 164 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37893
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
