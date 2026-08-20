# SyndProxy private pool

## Current pool

- Alive now: 769
- Gold now: 384
- HTTP: 205 alive / 74 gold
- HTTPS: 154 alive / 17 gold
- SOCKS4: 198 alive / 146 gold
- SOCKS5: 212 alive / 147 gold

## Historical pool

- Discovered: 148345
- Ever alive: 26420
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
