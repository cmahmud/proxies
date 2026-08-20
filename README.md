# SyndProxy private pool

## Current pool

- Alive now: 849
- Gold now: 394
- HTTP: 242 alive / 79 gold
- HTTPS: 198 alive / 19 gold
- SOCKS4: 210 alive / 157 gold
- SOCKS5: 199 alive / 139 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26819
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
