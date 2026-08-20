# SyndProxy private pool

## Current pool

- Alive now: 853
- Gold now: 392
- HTTP: 234 alive / 78 gold
- HTTPS: 202 alive / 20 gold
- SOCKS4: 209 alive / 148 gold
- SOCKS5: 208 alive / 146 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26819
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
