# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 366
- HTTP: 104 alive / 38 gold
- HTTPS: 49 alive / 11 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 188 alive / 159 gold

## Historical pool

- Discovered: 171593
- Ever alive: 32936
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
