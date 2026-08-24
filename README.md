# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 384
- HTTP: 131 alive / 63 gold
- HTTPS: 41 alive / 15 gold
- SOCKS4: 172 alive / 151 gold
- SOCKS5: 176 alive / 155 gold

## Historical pool

- Discovered: 176557
- Ever alive: 33207
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
