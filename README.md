# SyndProxy private pool

## Current pool

- Alive now: 683
- Gold now: 392
- HTTP: 188 alive / 67 gold
- HTTPS: 84 alive / 14 gold
- SOCKS4: 202 alive / 153 gold
- SOCKS5: 209 alive / 158 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25721
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
