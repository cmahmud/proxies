# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 346
- HTTP: 188 alive / 40 gold
- HTTPS: 69 alive / 9 gold
- SOCKS4: 173 alive / 152 gold
- SOCKS5: 188 alive / 145 gold

## Historical pool

- Discovered: 171044
- Ever alive: 32845
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
