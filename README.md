# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 442
- HTTP: 142 alive / 86 gold
- HTTPS: 64 alive / 24 gold
- SOCKS4: 164 alive / 162 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34246
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
