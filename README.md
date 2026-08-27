# SyndProxy validated proxy pool

## Current pool

- Alive now: 656
- Gold now: 404
- HTTP: 105 alive / 67 gold
- HTTPS: 181 alive / 14 gold
- SOCKS4: 176 alive / 157 gold
- SOCKS5: 194 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40618
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
