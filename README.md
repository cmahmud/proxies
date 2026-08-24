# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 443
- HTTP: 122 alive / 84 gold
- HTTPS: 83 alive / 24 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 191 alive / 173 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34191
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
