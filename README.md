# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 401
- HTTP: 123 alive / 79 gold
- HTTPS: 62 alive / 21 gold
- SOCKS4: 164 alive / 146 gold
- SOCKS5: 181 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48056
- Ever gold: 1516

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
