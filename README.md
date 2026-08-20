# SyndProxy private pool

## Current pool

- Alive now: 814
- Gold now: 400
- HTTP: 204 alive / 76 gold
- HTTPS: 168 alive / 19 gold
- SOCKS4: 219 alive / 154 gold
- SOCKS5: 223 alive / 151 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26778
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
