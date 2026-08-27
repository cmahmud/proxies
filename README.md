# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 410
- HTTP: 96 alive / 62 gold
- HTTPS: 158 alive / 19 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 197 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40720
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
