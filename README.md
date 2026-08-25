# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 417
- HTTP: 88 alive / 60 gold
- HTTPS: 66 alive / 21 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 189 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36147
- Ever gold: 1268

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
