# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 366
- HTTP: 94 alive / 51 gold
- HTTPS: 41 alive / 11 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 175 alive / 153 gold

## Historical pool

- Discovered: 174123
- Ever alive: 33056
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
