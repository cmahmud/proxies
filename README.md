# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 441
- HTTP: 123 alive / 86 gold
- HTTPS: 87 alive / 23 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34281
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
