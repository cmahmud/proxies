# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 466
- HTTP: 137 alive / 97 gold
- HTTPS: 57 alive / 39 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49373
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
