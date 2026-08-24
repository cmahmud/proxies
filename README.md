# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 389
- HTTP: 127 alive / 55 gold
- HTTPS: 47 alive / 12 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 200 alive / 164 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33374
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
