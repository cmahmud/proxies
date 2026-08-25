# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 423
- HTTP: 97 alive / 64 gold
- HTTPS: 115 alive / 26 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35826
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
